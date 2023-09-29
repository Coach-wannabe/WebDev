// Selectors
const input = document.querySelector('.todo-input');
const button = document.querySelector('.todo-button');
const list = document.querySelector('.todo-list');

// Event Listeners
button.addEventListener('click', addTask);
list.addEventListener('click', deleteTask);


// Functions
function addTask(event){
    event.preventDefault();

    const div = document.createElement("div");
    div.classList.add("todo");
    
    const completedButton = document.createElement('input');
    completedButton.setAttribute("type", "checkbox");
    completedButton.innerHTML = '<i></i>';
    completedButton.innerText = "check";
    completedButton.classList.add("check-box");
    div.appendChild(completedButton);

    const newTodo = document.createElement('li');
    newTodo.innerText = input.value;
    newTodo.classList.add('todo-item');
    div.appendChild(newTodo);
    
    const trashButton = document.createElement('img');
    trashButton.src = "trash-10-16.png";
    trashButton.innerHTML = '<i></i>';
    trashButton.classList.add("trash-btn");
    div.appendChild(trashButton);
    
    list.appendChild(div);

    input.value = "";
}

function deleteTask(event){
    const item = event.target;

    // Delete todo
    if(item.classList[0] === 'trash-btn'){
        const todo = item.parentElement;
        todo.classList.add("fall");

        todo.addEventListener("transitionend", function(){
            todo.remove();
        })
    }

    if(item.classList[0]  === "check-box"){
        const todo = item.parentElement;
        todo.classList.toggle("completed");
    }
}
