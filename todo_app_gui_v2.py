import json  # import module to save to disk

def save_tasks(task_list, filename="tasks.json"): # function takes task_list as a param, and defines tasks.json as location
    with open(filename, 'w') as f: # opens file as writeable and assigns to var f
        json.dump(task_list, f) # dump the data a json to disk
def load_tasks(filename="tasks.json"): # function to load from a file & defines file location
    try: # error handleing try statement
        with open(filename, 'r') as f: # opens file as readable
            return json.load(f) # json module method to load json file
    except FileNotFoundError: # Exception for no file
        return {} # If no file exists, return an empty dictionary

class TaskManager: # TaskManger class
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
            self.reindex_task_ids() # Re-index function
            print(f"Task {user_input} deleted successfully.")
        else:
            print("Invalid Task ID. Please try again.")

    def reindex_task_ids(self): # Re-index the task list starting from 1
        new_task_list = {} # Create a temp dict to move tasks into sequentially
        new_id = 1 # Indexing from 0
        for self.task_id, task_description in self.task_list.items(): # For id, desc, in task list. .items() method for dict iteration
            new_task_list[str(new_id)] = task_description # Similar to update method used in add task
            new_id += 1 # Increment
        self.task_list = new_task_list # set task_list from temp dict
        self.task_id = len(self.task_list)+1 # reset task_id idx at len+1

    def return_to_options(self): # Allows for the screen to pause before advancing
        input("Press enter to return to main menu.")

    # main function containing while running and conditional logic
    def run(self):
        user_input = ""
        running = True
        while running: # Text based UI
            print("please select one of the following options:")
            print('-------------------------------------------')
            print('1. Add a new item to the list')
            print('2. Delete an item from the list')
            print('3. Show To Do List')
            print('4. Save To Do List to Disk')
            print('5. Save & Exit App')
            # User input
            user_input = input("Enter 1-5: ")
            match user_input: # Python Switch method
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


if __name__ == "__main__": # Run the app
    TaskManager().run() # Explicitly call TaskManger run