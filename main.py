import gradio as gr
import pandas as pd

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append({"Task": task_description, "Completed": False})
        return pd.DataFrame(self.tasks)

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index]
            return pd.DataFrame(self.tasks)
        except IndexError:
            return pd.DataFrame(self.tasks)

    def mark_completed(self, task_index):
        try:
            self.tasks[task_index]["Completed"] = True
            return pd.DataFrame(self.tasks).astype({"Completed": bool})
        except IndexError:
            return pd.DataFrame(self.tasks).astype({"Completed": bool})

    def mark_not_completed(self, task_index):
        try:
            self.tasks[task_index]["Completed"] = False
            return pd.DataFrame(self.tasks).astype({"Completed": bool})
        except IndexError:
            return pd.DataFrame(self.tasks).astype({"Completed": bool})

    def update_task(self, task_index, task_description):
        try:
            self.tasks[task_index]["Task"] = task_description
            return pd.DataFrame(self.tasks)
        except IndexError:
            return pd.DataFrame(self.tasks)

def main():
    todo_list = ToDoList()

    def update(task_description, task_index, action, new_task_description):
        if action == "Add Task":
            return todo_list.add_task(task_description)
        elif action == "Delete Task":
            if task_index is not None and len(todo_list.tasks) > 0:
                return todo_list.delete_task(int(task_index) - 1)
            else:
                return pd.DataFrame(columns=["Task", "Completed"])
        elif action == "Mark Task as Completed":
            if task_index is not None and len(todo_list.tasks) > 0:
                return todo_list.mark_completed(int(task_index) - 1)
            else:
                return pd.DataFrame(columns=["Task", "Completed"])
        elif action == "Mark Task as Not Completed":
            if task_index is not None and len(todo_list.tasks) > 0:
                return todo_list.mark_not_completed(int(task_index) - 1)
            else:
                return pd.DataFrame(columns=["Task", "Completed"])
        elif action == "Update Task":
            if task_index is not None and len(todo_list.tasks) > 0:
                return todo_list.update_task(int(task_index) - 1, new_task_description)
            else:
                return pd.DataFrame(columns=["Task", "Completed"])

    demo = gr.Interface(
        fn=update,
        inputs=[
            gr.Textbox(label="Task Description"),
            gr.Number(label="Task Index", value=1),
            gr.Radio(["Add Task", "Delete Task", "Mark Task as Completed", "Mark Task as Not Completed", "Update Task"], label="Action"),
            gr.Textbox(label="New Task Description")
        ],
        outputs=gr.Dataframe(headers=["Task", "Completed"]),
        title="To-Do List",
        description="Manage tasks from the command line"
    )

    demo.launch()

if __name__ == "__main__":
    main()