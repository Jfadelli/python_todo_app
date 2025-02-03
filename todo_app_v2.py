import json  # import module to save to disk


# function takes task_list as a param, and defines tasks.json as location
def save_tasks(task_list, filename="tasks.json"):
    with open(filename, 'w') as f:                  # opens file as writeable and assigns to var f
        # dump the data a json to disk
        json.dump(task_list, f)


# function to load from a file & defines file location
def load_tasks(filename="tasks.json"):
    try:                                            # error handleing try statement
        with open(filename, 'r') as f:              # opens file as readable
            # json module method to load json file
            return json.load(f)
    except FileNotFoundError:                       # Exception for no file
        # If no file exists, return an empty dictionary
        return {}


class TaskManager:                                                      # TaskManger class
    def __init__(self):
        self.task_list = load_tasks()
        self.task_id = len(self.task_list)+1

    def add_task(self):
        task_description = input("Task Description: ")
        self.task_list.update({self.task_id: task_description})
        self.task_id += 1

    def list_tasks(self):
        if not self.task_list:
            print("\nNo tasks available.")
        else:
            print("\nTask List:")
            for key, task in self.task_list.items():
                print(f"{key}: {task}")

    def delete_task(self):
        user_input = input("Input ID of task to be deleted: ")
        if user_input in self.task_list:
            del self.task_list[user_input]
            self.reindex_task_ids()                                     # Re-index function
            print(f"Task {user_input} deleted successfully.")
        else:
            print("Invalid Task ID. Please try again.")

    # Re-index the task list starting from 1
    def reindex_task_ids(self):
        # Create a temp dict to move tasks into sequentially
        new_task_list = {}
        # Indexing from 0
        new_id = 1
        # For id, desc, in task list. .items() method for dict iteration
        for self.task_id, task_description in self.task_list.items():
            # Similar to update method used in add task
            new_task_list[str(new_id)] = task_description
            new_id += 1                                                 # Increment
        # set task_list from temp dict
        self.task_list = new_task_list
        # reset task_id idx at len+1
        self.task_id = len(self.task_list)+1

    # Allows for the screen to pause before advancing
    def return_to_options(self):
        input("Press enter to return to main menu.")

    # main function containing while running and conditional logic
    def run(self):
        user_input = ""
        running = True
        while running:
            # Text based UI
            print("please select one of the following options:")
            print('-------------------------------------------')
            print('1. Add a new item to the list')
            print('2. Delete an item from the list')
            print('3. Show To Do List')
            print('4. Save To Do List to Disk')
            print('5. Save & Exit App')
            # User input
            user_input = input("Enter 1-5: ")
            match user_input:                                           # Python Switch method
                case "1":
                    self.add_task()
                case "2":
                    self.list_tasks()
                    self.delete_task()
                    self.list_tasks()
                case "3":
                    self.list_tasks()
                    self.return_to_options()
                case "4":
                    save_tasks(self.task_list)
                case "5":
                    save_tasks(self.task_list)
                    print('Saving To Do Task List to disk...')
                    print("Quitting gracefully.")
                    running = False


if __name__ == "__main__":                                              # Run the app
    # Explicitly call TaskManger run
    TaskManager().run()
