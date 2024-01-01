> # Описание проекта
Цирроз возникает в результате длительного повреждения печени, приводящего к образованию обширных рубцов, часто из-за таких состояний, как гепатит или хроническое употребление алкоголя. Используя 17 клинических признаков спрогнозировать состояние выживаемости пациентов с циррозом печени.
> # Навыки и инструменты
- pandas 
- numpy 
- seaborn
- matplotlib.pyplot
- optuna

- sklearn.preprocessing.StandardScaler
- sklearn.preprocessing.OneHotEncoder
- sklearn.model_selection.train_test_split
- sklearn.model_selection.GridSearchCV
- sklearn.compose.make_column_selector
- sklearn.compose.make_column_transformer
- sklearn.pipeline.Pipeline
- sklearn.metrics.log_loss
- sklearn.ensemble.RandomForestClassifier
- sklearn.ensemble.,GradientBoostingClassifier
- sklearn.tree import DecisionTreeClassifier
- sklearn.linear_model.LogisticRegression
- sklearn.cluster.KMeans
- catboost.CatBoostClassifier
- xgboost.XGBClassifier
> # Общий вывод
- Модели CatBoosr, GradientBoosting и XGB показывают близкие результаты метрики качества log loss. Для улучшения результатов стоит применить Feature Engineering и кластеризацию попарных признаков.
- На тестовой выборке получилось достичь значения метрики log_loss равное 0.41.
- Данный результат метрики превышает 80% верных предсказаний классов.

