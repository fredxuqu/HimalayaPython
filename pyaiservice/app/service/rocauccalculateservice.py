"""
    create by Fred on 2018/8/22
"""
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from app.config.settings import GLOBAL_PAGE_SIZE
from app.utils.json import to_json
from app.utils.logger import Logger
from app.dto.points import XYPoints
from app.dto.rocaucresult import RocAucResult
from app.repository.pymysql.modelestimaterepository import ModelEstimateRepository
from app.repository.pymysql.samplerepository import SampleRepository

import json

__author__ = 'Fred'


repository = ModelEstimateRepository()


# calculate ROC and AUC
class ROCAUCCalculateService:

    @classmethod
    def cal_roc_auc(cls, v_sample_ids, v_model_id, v_strategy_id):
        sample_id_list = v_sample_ids.split(',')
        roc_auc_result = list()
        for sample_id in sample_id_list:
            roc_auc = ROCAUCCalculateService.cal_roc_auc_per_sample(sample_id, v_model_id, v_strategy_id)
            if roc_auc is not None:
                roc_auc_result.append(roc_auc)
        return roc_auc_result

    @classmethod
    def cal_roc_auc_per_sample(cls, v_sample_id, v_model_id, v_strategy_id):
        if v_strategy_id is not None and len(v_strategy_id) > 0:
            return ROCAUCCalculateService.cal_roc_auc_by_strategy(v_sample_id, v_model_id, v_strategy_id)
        else:
            return ROCAUCCalculateService.cal_roc_auc_by_model(v_sample_id, v_model_id)

    @classmethod
    def cal_roc_auc_by_model(cls, v_sample_id, v_model_id):
        # get data from data base
        current_page = 1
        all_sample_records = []
        while True:
            sample_page_list = ModelEstimateRepository\
                .query_sample_model_records_paginate(v_sample_id, v_model_id, GLOBAL_PAGE_SIZE, current_page, False)
            if sample_page_list is not None and len(sample_page_list) > 0:
                for item in sample_page_list:
                    all_sample_records.append(item)
                current_page = current_page + 1
            else:
                break
        # calculate
        return ROCAUCCalculateService.cal_roc_auc_by_all_sample(v_sample_id, all_sample_records)

    @classmethod
    def cal_roc_auc_by_strategy(cls, v_sample_id, v_model_id, v_strategy_id):
        # get data from data base
        current_page = 1
        all_sample_records = []
        while True:
            sample_page_list = ModelEstimateRepository.query_sample_model_strategy_records_paginate(
                                v_sample_id, v_model_id, v_strategy_id, GLOBAL_PAGE_SIZE, current_page, False)
            if sample_page_list is not None and len(sample_page_list) > 0:
                for item in sample_page_list:
                    all_sample_records.append(item)
                current_page = current_page + 1
            else:
                break
        # calculate
        return ROCAUCCalculateService.cal_roc_auc_by_all_sample(v_sample_id, all_sample_records)

    @classmethod
    def cal_roc_auc_by_all_sample(cls, v_sample_id, all_sample_records):

        if all_sample_records is None or len(all_sample_records) <= 0:
            return None

        # put sample result and pre estimate score to different list.
        y_true_result = []
        y_scores = []
        for item in all_sample_records:
            if item[1] is not None and item[2] is not None:  # remove all invalid sample
                y_scores.append(item[1])
                y_true_result.append(int(item[2]))

        # call sklearn to calculate roc and auc, then put the result to RocAucResult and load as a json
        Logger.debug(to_json(y_true_result))
        Logger.debug(to_json(y_scores))
        fpr, tpr, _ = roc_curve(np.array(y_true_result), np.array(y_scores))
        Logger.debug(tpr)
        Logger.debug(fpr)

        auc = roc_auc_score(np.array(y_true_result), np.array(y_scores))
        Logger.debug(to_json(auc))

        # encapsulate fpr, tpr and auc to RocAucResult
        roc_points = []
        index = 0
        fpr_size = len(fpr)
        while index < fpr_size:
            point = XYPoints(round(fpr[index], 2), round(tpr[index], 2))  # fpr is x axis, tpr is y axis
            roc_points.append(json.loads(json.dumps(point, default=lambda o: o.__dict__, sort_keys=True, indent=4)))
            index = index + 1

        roc_auc = RocAucResult(None, None, roc_points, round(auc, 2))

        roc_auc.sample_id = v_sample_id
        sample_model = SampleRepository.query_sample_by_id(v_sample_id)
        roc_auc.sample_name = sample_model.name
        Logger.debug(to_json(json.loads(json.dumps(roc_auc, default=lambda o: o.__dict__, sort_keys=True, indent=4))))
        # return
        return roc_auc
