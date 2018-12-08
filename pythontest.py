#!python
a = 3+4+5
b = a/3
print("content-type: text/html; charset=UTF-8\n")
print('''
<html>
<head>
  <title>제목이다임마</title>
  <meta charset="UTF-8" />
</head>
<body>
  <h1>소제목이당</h1>

<style>
  a {
    color:red;
  }
  h1 {
    font-size:60px;
    text-align: center;
    border-bottom:1px solid gray;
    padding:20px;
    margin-bottom:0;
  }
  ol {
    border-right:1px solid gray;
    width:150px;
    margin:0;
    padding:20px;
  }
  body {
    margin:0;
  }
  .ex {
    font-size:20px;
  }
  #grid {
    border:2px solid pink;
    display:grid;
    grid-template-columns:500px 1fr;
  }
</style>

<input type="button" value="night" onclick="
  var target = document.querySelector('body');
      if(this.value === 'night'){
    target.style.backgroundColor='black';
    target.style.color='white';
    this.value='day';
  } else {
    target.style.backgroundColor='white';
    target.style.color='black';
    this.value='night';
  }
">

<div id="grid">
  <ol>
    <li style="color:blue ">오뎅</li>
    <li class="ex">떠뽀끼</li>
    <a href="http://google.com" target="_blank" title="마우스설명"> 호떡</a>
    <a href="http://naver.com" target="_blank" title="네이놈"> 김치</a>
  </ol>

  <div>
  <input type="button" value="넌누구냐" onclick="alert('알것없어')">
  <input type="text" onchange="alert('머라구')">
  <input type="text" onkeydown="alert('모개')">


  <input type="button" value="night" onclick="
    var target = document.querySelector('body');
        if(this.value === 'night'){
      target.style.backgroundColor='black';
      target.style.color='white';
      this.value='day';

      var links = document.querySelectorAll('a');
      var i = 0;
      while(i<links.length){
        links[i].style.color='powderblue';
        i=i+1;
      }
    } else {
      target.style.backgroundColor='white';
      target.style.color='black';
      this.value='night';

      var links = document.querySelectorAll('a');
      var i = 0;
      while(i<links.length){
        links[i].style.color='blue';
        i=i+1;
    }
  ">
</div>
</div>

</body>
</html>
''')
