
from config.celery_app import app

celery_inspector = app.control.inspect()


class CeleryHelper:

    @staticmethod
    def is_being_executed(task_name, *args, **kwargs):
        """
        Returns whether the task with given task_name is already being executed.
        """
        args_list = list(args)
        active_tasks = app.control.inspect().active()
        if active_tasks:
            for worker, running_tasks in active_tasks.items():
                for task in running_tasks:
                    if task["name"] == task_name and task['args'] == args_list:
                        return True

        return False
