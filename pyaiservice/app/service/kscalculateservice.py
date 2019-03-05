"""
    create by Fred on 2018/8/22
"""
from app.config.settings import GLOBAL_PAGE_SIZE
from app.config.settings import KS_SHARD_NUM
from app.utils.json import to_json
from app.utils.logger import Logger
from app.dto.ksshard import KSShardRule
from app.dto.ksresult import KSResult
from app.dto.ksshardresult import KSShardResult
from app.repository.pymysql.modelestimaterepository import ModelEstimateRepository
from app.repository.pymysql.samplerepository import SampleRepository


__author__ = 'Fred'


repository = ModelEstimateRepository()


# calculate ks
class KSCalculateService:

    @classmethod
    def cal_ks(cls, v_sample_ids, v_model_id, v_strategy_id):
        sample_id_list = v_sample_ids.split(',')
        ks_result = list()
        for sample_id in sample_id_list:
            ks = KSCalculateService.cal_ks_by_sample(sample_id, v_model_id, v_strategy_id)
            if ks is not None:
                ks_result.append(ks)
        return ks_result

    @classmethod
    def cal_ks_by_sample(cls, v_sample_id, v_model_id, v_strategy_id):
        if v_strategy_id is not None and len(v_strategy_id) > 0:
            return KSCalculateService.cal_ks_by_strategy(v_sample_id, v_model_id, v_strategy_id)
        else:
            return KSCalculateService.cal_ks_by_model(v_sample_id, v_model_id)

    @classmethod
    def cal_ks_by_model(cls, v_sample_id, v_model_id):
        current_page = 1
        all_sample_records = []
        while True:
            sample_page_list = ModelEstimateRepository\
                .query_sample_model_records_paginate(v_sample_id, v_model_id, GLOBAL_PAGE_SIZE, current_page, True)
            #  True means that sorting type is ascending
            if sample_page_list is not None and len(sample_page_list) > 0:
                for item in sample_page_list:
                    all_sample_records.append(item)
                current_page = current_page + 1
            else:
                break

        Logger.debug(to_json(all_sample_records))

        # get sharding rules
        ks_shards = KSCalculateService.split_samples(all_sample_records)

        # calculate
        return KSCalculateService.cal_ks_by_default(v_sample_id, ks_shards, all_sample_records)

    @classmethod
    def cal_ks_by_strategy(cls, v_sample_id, v_model_id, v_strategy_id):
        # get data from data base
        current_page = 1
        all_sample_records = []
        while True:
            sample_page_list = ModelEstimateRepository.query_sample_model_strategy_records_paginate(
                                v_sample_id, v_model_id, v_strategy_id, GLOBAL_PAGE_SIZE, current_page, True)
            if sample_page_list is not None and len(sample_page_list) > 0:
                for item in sample_page_list:
                    all_sample_records.append(item)
                current_page = current_page + 1
            else:
                break

        Logger.debug(to_json(all_sample_records))

        # get sharding rules
        ks_shards = KSCalculateService.split_samples(all_sample_records)

        # calculate
        return KSCalculateService.cal_ks_by_default(v_sample_id, ks_shards, all_sample_records)

    # default split rule, equally divided samples into 10
    @classmethod
    def split_samples(cls, all_sample_records):
        ks_shards = []
        # calculate sample records count
        sample_size = len(all_sample_records)

        # default shard number is 10
        shard_num = 10
        if KS_SHARD_NUM is not None:
            shard_num = KS_SHARD_NUM

        # calculate per shard page size
        shard_page_size = sample_size // KS_SHARD_NUM

        index = 0
        score_start = None
        score_end = None
        while index < shard_num:
            current_split_point = index * shard_page_size + shard_page_size
            if index == shard_num - 1:   # the last shard
                score_end = None
                shard = KSShardRule("", score_start, score_end)
                ks_shards.append(shard)
                score_start = score_end
            else:
                # format of sample ("batno", result, score)
                sample = all_sample_records[current_split_point]
                score_end = sample[1]
                shard = KSShardRule("", score_start, score_end)
                ks_shards.append(shard)
                score_start = score_end
            index = index + 1

        Logger.debug(to_json(ks_shards))

        return ks_shards

    # Default method, equal split samples into 10 segments by score
    @classmethod
    def cal_ks_by_default(cls, v_sample_id, v_ks_shards, v_all_sample_records):
        # calculate
        if v_all_sample_records is None or len(v_all_sample_records) <= 0:
            return None

        ks_sharps_results = []

        # total sample count
        total_sample_size = len(v_all_sample_records)

        # calculate good and bad sample count
        v_good_total_count = 0
        v_bad_total_count = 0
        for sample in v_all_sample_records:
            # 0 : good, 1: bad
            if sample[2] == "0":
                v_good_total_count = v_good_total_count + 1
            else:
                v_bad_total_count = v_bad_total_count + 1

        # get sample detail information
        sample_info = SampleRepository.query_sample_by_id(v_sample_id)

        index = 0
        v_good_count = 0
        v_bad_count = 0
        v_ks = 0.0

        for ks_sharp in v_ks_shards:
            v_good_count_per_shard = 0
            v_bad_count_per_shard = 0
            v_total_count_per_shard = 0
            while index < total_sample_size:
                sample = v_all_sample_records[index]
                # exception , both start and end are None
                if ks_sharp.score_start is None and ks_sharp.score_end is None:
                    Logger.error("Error: both start and end are None!")
                    break
                # if current sample belong current shard
                if (ks_sharp.score_start is None and sample.score < ks_sharp.score_end) \
                        or (ks_sharp.score_end is None and sample.score >= ks_sharp.score_start) \
                        or (ks_sharp.score_start is not None
                            and ks_sharp.score_end is not None
                            and ks_sharp.score_start <= sample.score < ks_sharp.score_end):
                    # identify good and bad sample
                    if sample[2] == "0":
                        v_good_count = v_good_count + 1
                        v_good_count_per_shard = v_good_count_per_shard + 1
                    else:
                        v_bad_count = v_bad_count + 1
                        v_bad_count_per_shard = v_bad_count_per_shard + 1
                else:
                    break

                v_total_count_per_shard += 1
                index = index + 1
                # end while

            # KSShardResult(v_shard_name, v_count_bad, v_ratio_bad, v_count_good, v_ratio_good)
            v_ratio_good = round(v_good_count/v_good_total_count, 4)
            v_ratio_bad = round(v_bad_count / v_bad_total_count, 4)

            # calculate KS
            ks_per_shard = abs(v_ratio_good - v_ratio_bad)
            if ks_per_shard > v_ks:
                v_ks = round(ks_per_shard, 4)
            v_shard_name = ks_sharp.shard_name
            if v_shard_name is None or len(v_shard_name) <= 0:
                if ks_sharp.score_start is None:
                    v_shard_name = "Low - <" + str(ks_sharp.score_end)
                elif ks_sharp.score_end is None:
                    v_shard_name = str(ks_sharp.score_start) + " - High"
                else:
                    v_shard_name = str(ks_sharp.score_start) + " - <" + str(ks_sharp.score_end)

            ks_shard_result = KSShardResult(v_shard_name, v_bad_count_per_shard, v_ratio_bad, v_good_count_per_shard
                                            , v_ratio_good, v_total_count_per_shard, round(ks_per_shard, 4))
            ks_sharps_results.append(ks_shard_result)
            # end for

        # print
        Logger.debug(to_json(ks_sharps_results))

        ks_result = KSResult(sample_info.id, sample_info.name, ks_sharps_results, v_ks, total_sample_size, v_good_count,
                             v_bad_count)
        # return
        return ks_result
