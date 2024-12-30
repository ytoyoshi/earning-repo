import { useState } from 'react'
import { InputTodo } from './components/InputTodo';

import './App.css'
import { IncompleteTodoList } from './components/IncompleteTodoList';
import { CompleteTodoList } from './components/CompleteTodoList';

function App() {
  const [todoText, setTodoText] = useState("");
  const [incompleteTodoList, setIncompleteTodoList] = useState([]);
  const [completeTodoList, setCompleteTodoList] = useState([]);

  const onChageTodoText = (event) => setTodoText(event.target.value);

  const onClickAdd = () =>{
    if (todoText ==="") return;
    const newTodoList = [...incompleteTodoList, todoText]
    setIncompleteTodoList(newTodoList)
    setTodoText("")
  }

  const onClickComplete = (index) =>{
    const compoleteTodo = incompleteTodoList[index]
    const newCompleteTodoList = [...completeTodoList, compoleteTodo]
    setCompleteTodoList(newCompleteTodoList)
    const newIncompleteTodoList = [...incompleteTodoList]
    newIncompleteTodoList.splice(index,1)
    setIncompleteTodoList(newIncompleteTodoList)
  }

  const onClickDelete = (index) =>{
    const newIncompleteTodoList = [...incompleteTodoList]
    newIncompleteTodoList.splice(index,1)
    setIncompleteTodoList(newIncompleteTodoList)
  }

  const onClickBack = (index) =>{
    const backTodo = completeTodoList[index]
    const newCompleteTodoList = [...completeTodoList]
    newCompleteTodoList.splice(index, 1)
    setCompleteTodoList(newCompleteTodoList)
    const newIncompleteTodoList = [...incompleteTodoList, backTodo]
    setIncompleteTodoList(newIncompleteTodoList)
  }

  return (
    <>
      <div>
        <InputTodo
          todoText={todoText}
          onChangeTodoText={onChageTodoText}
          onClickAdd={onClickAdd}
        />
      </div>
      <div>
        <IncompleteTodoList
          todos={incompleteTodoList}
          onClickComplete={onClickComplete}
          onClickDelete={onClickDelete}
        />
      </div>
      <div>
        <CompleteTodoList
          todos={completeTodoList}
          onClickBack={onClickBack}
        />
      </div>
    </>
  )
}

export default App
