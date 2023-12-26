> # Описание проекта
Компания «Чётенькое такси» собрала исторические данные о заказах такси в аэропортах. Чтобы привлекать больше водителей в период пиковой нагрузки, нужно спрогнозировать количество заказов такси на следующий час. Требуется построить модель для такого предсказания.
> # Навыки и инструменты
- pandas
- matplotlib
- statsmodels
- sklearn.model_selection.train_test_split
- sklearn.model_selection.TimeSeriesSplit
- sklearn.linear_model.LinearRegression
- sklearn.linear_model.Lasso
- sklearn.ensemble.GradientBoostingRegressor
- sklearn.metrics.mean_squared_error
- sklearn.pipeline.Pipeline
- sklearn.preprocessing.StandardScaler
- lightgbm.LGBMRegressor
- skopt.BayesSearchCV
> # Общий вывод
- На тестовой выборке получилось достичь значения метрики RMSE равное 43.23, что соответствует условию задания.
- Количество признаков "отстающее значение" пришлось довести до 24 для достижения необходимого результата.
- Из календарных признаков достаточно два: 1) номер месяца; 2) номер недели.
- Во временном ряде наблюдается восходя тренд, число заказов с начала марта по конец августа стремительно растет.
