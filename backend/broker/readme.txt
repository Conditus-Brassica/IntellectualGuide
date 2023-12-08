При создании функции агента, которая может быть вызвана другим агентом,
необходимо создать для нее broker task-и в модуле agents_tasks и метод в AgentsBroker для вызова этого task-а.
Метод, вызывающий task, так же должен быть объявлен в PureBroker с реализацией raise NotImplementedError
(метод имеет спецификацию @classmethod и в PureBroker, и в AgentsBroker).

taskiq broker:broker agents_tasks:my_task agents_task:my_task1

Где my_task, my_task1 - это название py файлов где лежат task для конкретного агента.
Необходимо перечислить все.
