# Import necessary libraries
import streamlit as st

# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_task(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_task(self, index):
        n = int(index) - 1
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == n:
            self.remove_first_task()
        else:
            while current_node != None and position + 1 != n:
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Insert not present")


    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.data)
            current = current.next

        return tasks

# Create a Streamlit app
def main():
    st.title("To-Do List App with Linked List")

    # Initialize a linked list
    if 'tasks_list' not in st.session_state:
        st.session_state.tasks_list = LinkedList()

    # Sidebar for adding tasks
    task_input = st.sidebar.text_input("Add Task:")
    if st.sidebar.button("Add"):
        if task_input:
            st.session_state.tasks_list.add_task(task_input)

    # Sidebar for removing tasks
    task_to_remove = st.sidebar.text_input("Remove Task (Enter the Number of Task's order):")
    if st.sidebar.button("Remove"):
        if task_to_remove:
            st.session_state.tasks_list.remove_task(task_to_remove)

    # Sidebar option to view tasks
    tasks = st.session_state.tasks_list.display_tasks()
    st.write("## Your To-Do List:")
    if not tasks:
        st.write("No tasks yet. Add some tasks using the sidebar!")
    for i, task in enumerate(tasks, start=1):
        st.write(f"{i}. {task}")

if __name__ == "__main__":
    main()
