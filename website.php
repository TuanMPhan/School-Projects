<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="align.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css">
    
<?php
    function retrieve($city) {
        $ct = $city;
        $cnx = new mysqli('localhost', 'tp', 'bi646999', 'weather');

        if ($cnx->connect_error)
            die('Connection failed: ' . $cnx->connect_error);

        $query = sprintf('SELECT * FROM %s',$ct); 
        $cursor = $cnx->query($query);
        $message = sprintf('Five days weather forecast in %s',$ct);
        echo $message;
        while ($row = $cursor->fetch_assoc()) {
            echo '<tr>';
            echo '<td>' . $row['date'] . '</td><td>' . $row['dayOrNight'] . '</td><td align="right">' . $row['short_desc'] .'</td><td align="right">' . $row['temperature'] .'</td><td align="right">' . $row['long_desc'] .'</td>';
            echo '</tr>';
        }
        $cnx->close();
    }  
?>

    <title>Jersey's Weather Forecast</title>
</head>
<body>
    <h1><center class="title">New Jersey's Five Days Weather Forecast</center></h1>
    <form method="post">
        <div class="items">
            <div class="item">
                <button class="button" type="submit" name="newark"> <img src="weather.png" height ="130" width="140" /></button>
                <label class="add-fav">
                    <input type="checkbox" />
                    <i class="icon-heart">
                        <i class="icon-plus-sign"></i>
                    </i>
                </label>
                <span class="caption">Newark</span>
            </div>
            <div class="item">
                <button type="submit" name="hoboken"> <img src="weather.png" height ="130" width="140" /></button>
                <label class="add-fav">
                    <input type="checkbox" />
                    <i class="icon-heart">
                        <i class="icon-plus-sign"></i>
                    </i>
                    </label>
                <span class="caption">Hoboken</span>
            </div>
            <div class="item">
                <button type="submit" name="hackensack"> <img src="weather.png" height ="130" width="140" /></button>
                <label class="add-fav">
                    <input type="checkbox" />
                    <i class="icon-heart">
                        <i class="icon-plus-sign"></i>
                    </i>
                    </label>
                <span class="caption">Hackensack</span>
            </div>
            <div class="item">
                <button type="submit" name="princeton" > <img src="weather.png" height ="130" width="140" /></button>
                <label class="add-fav">
                    <input type="checkbox" />
                    <i class="icon-heart">
                        <i class="icon-plus-sign"></i>
                    </i>
                    </label>
                <span class="caption">Princeton</span>
            </div>
            <div class="item">
                <button type="submit" name="trenton"> <img src="weather.png" height ="130" width="140" /></button>
                <label class="add-fav">
                    <input type="checkbox" />
                    <i class="icon-heart">
                        <i class="icon-plus-sign"></i>
                    </i>
                    </label>
                <span class="caption">Trenton</span>
            </div>    
        </div>
    </form>

<table align="center" border="1">
<?php
    if(isset($_POST['newark'])){
        retrieve('newark');
    }
    else if (isset($_POST['hoboken'])){
        retrieve('hoboken');
    }
    else if (isset($_POST['hackensack'])){
        retrieve('hackensack');
    }
    else if (isset($_POST['princeton'])){
        retrieve('princeton');
    }
    else if (isset($_POST['trenton'])){
        retrieve('trenton');
    }
?>
</table>


</body>
</html>