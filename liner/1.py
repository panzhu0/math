# 线性回归
import numpy as np
from util import preparation

class LinearRegression:
    def __init__(self,data,labels,polynomial_degree = 0,sinusoid_degree = 0,normalize_data = True):
        """
        1. 对数据进行预处理操作
        2. 得到所有的特征个数
        3. 初始化参数矩阵
        """

    def train(self,alpha,num_iterations = 500):
        cost_history = self.gradient_descent(alpha,num_iterations)
        return self.theta,cost_history

    def gradient_descent(self,alpha,num_iterations):
        cost_history = []
        for _ in range(num_iterations):
            # 完成一次梯度下降
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data,self.label))

    def cost_function(self,data,label):
        """计算损失值"""
        num_examples = data.shape[0]
        delta = LinearRegression.hypothsis(self.data,self.theta) - label
        cost = (1/2)*np.dot(delta.T,delta) # 计算残差平方
        return cost[0][0]   

    def gradient_step(self,alpha):
        """"梯度下降参数更新计算方法 (使用矩阵运算 而不用FOR 循环计算)"""
        num_examples = self.data.shape[0]
        # 预测值
        prediction = LinearRegression.hypothsis(self.data,self.theta)
        delta = prediction - self.label # 残差: 预测-真实  h_{\theta} (x^K) - y^K
        # 求\theta
        theta = self.theta
        theta = theta \
            - alpha  * (1/num_examples) \
                * ( np.dot(delta.T,self.data) ).T

        # 更新\theta
        self.theta = theta

    
    @staticmethod
    def hypothsis(data,theta):
        predictions = np.dot(data,theta)
        return predictions


    # 数据可视化
    def get_cost(self,data,labels):
        # 数据预处理
        data_processed = prepare_for_training(data,self.polynomial_degree,self.sinusoid_degree,self.normalize_data)[0]
        # 计算损失
        return self.cost_function(data_processed,labels)

    