<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>findDonor</title>
</head>

<body>

    <?php
    include 'config.php';

    $servername = "localhost";
    $username = "root";
    $password = $adminPassword;
    $database = "lab7_db";

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $database);

    // Check connection
    if (!$conn) {
        die("Connection to MySQL failed: " . mysqli_connect_error());
    }

    ?>

    <div class="container2">
        <div class="brand-title">FIND A DONOR</div>
        <div class="inputs">
            <form action="display.php" method="post">

                <label>Blood Group</label>
                <input type="text" name="donor_bloodgroup" placeholder="Enter Bloodgroup" />

                <button type="submit">SUBMIT</button>
            </form>
        </div>
    </div>

</body>

</html>