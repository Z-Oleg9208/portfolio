> # Описание проекта
Предоставлены пробы нефти в трёх регионах: в каждом 10 000 месторождений, где измерили качество нефти и объём её запасов. Необходимо построить модель машинного обучения, которая поможет определить регион, где добыча принесёт наибольшую прибыль
> # Навыки и инструменты
- pandas
- numpy
- sklearn.tree.DecisionTreeRegressor
- sklearn.ensemble.RandomForestRegressor
- sklearn.linear_model.LinearRegression 
- sklearn.model_selection.train_test_split
- sklearn.model_selection.GridSearchCV
- sklearn.metrics.r2_score
- sklearn.metrics.mean_squared_error
- sklearn.preprocessing.StandardScaler
- sklearn.dummy.DummyRegressor
- scipy.stats
> # Общий вывод
- Второй регион наиболее предпочтительный для дальнейшей разработки скважин.
- Модель во втором региони предсказывает значения целевого признака максимально близкие к реальным данным в то время как в первом и третьем регионах срезднее отклонение предсказания равняется 37 и 39 пр и средних значениях в 92 и 94 баррелей, что является погрешностью примерно в 40%.
- При применении техники Bootstrap риск убытков во втором регионее равен 1% в то время как в первом и третьем регионах риск значительно выше 5.6% и 6.6% соответственно.
- 95% доверительный интервал в первом и третьем регионах имеет отрицательные значения от 0.25 квартиля. Во втором регионе 95% доверительный интервал не имеет отрицательных значений прибыли.
- Во втором регионе средняя прибыль при применении техники Bootstrap равна 452932.19, что выше в двух других регионах.
