При создании функции агента, которая может быть вызвана другим агентом,
необходимо создавать ее с декоратором @BROKER.task, где BROKER - переменная в модуле agents_broker.
В task-е вызывается метод конкретного агента, а не абстрактного. Для вызова task-а необходимо передать его в качестве
параметра в метод AgentBroker.call_agent_tasks(agent_task, json_params)

При текущей реализации call_agent_task при вызове скорее всего будет оборачиваться в asyncio.create_task(...)

run from course directory:

taskiq worker backend.broker.agents_broker:BROKER backend.broker.agents_tasks


Возможно, таски придется в один файл закинуть, но пока что пишем файл с тасками на агента.
