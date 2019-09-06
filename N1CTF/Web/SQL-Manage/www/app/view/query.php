<!DOCTYPE html>
<html lang="en" >
<head>
    <meta charset="UTF-8">
    <title>Login form with confirmation!</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
<a href="#"id="logout">logout</a>
<h1 id="title">Welcome to N1CTF2019!!</h1>
<h1 id="title">You can connect to your mysql to execute SQL statement</h1>
<div class="container">
    <div class="loginBox">
        <div class="userImage">
            <img src="static/img/catFace.png">
        </div>
        <form id="loginForm">
            <div class="input-wrapper">
                <label>dbname:</label>
                <input type="input" name="dbname" placeholder="test" id="dbname">
            </div>
            <div class="input-wrapper">
                <label>query:</label>
                <input type="input" name="query" placeholder="select 1;" id="query">
            </div>
            <div class="input-wrapper">
                <label>result:</label>
                <br>
            </div>
            <div class="input-wrapper">
                <p id="news"></p>
            </div>
            <input type="button" name="" value="Submit" id="button">
        </form>
    </div>
</div>

<script src='static/js/jquery.min.js'></script>
<script src="static/js/query.js"></script>
</body>
</html>