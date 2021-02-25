# 나는 React를 알고싶다..
---
개발을 잘하고 싶다.. 깊이 있게 잘 아는 사람이 되고 싶다. 제발.

## Tic Tac Toe
React 공식 홈페이지에 있는 자습서를 실습해 보았다. 그리고 더해서 사각형들을 만들 때 하드코딩 대신에 두 개의 반복문을 사용하도록 Board를 다시 작성해주세요.를 구현해 보았다.
```javascript
  renderSquares() {
    let content = [];
    
    for (let i = 0; i < 3; i++) {
        let element = [];
        for (let j = 0; j < 3; j++) {
               element.push(this.renderSquare((i * 3) + j));
        }
        content.push(<div key={i} className="board-row">{element}</div>);
    }
    
    return content;
  }
```

for문을 사용해서 요소르 추가하는 방법을 알게 되었다.
