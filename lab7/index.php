<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Home&InsertPage</title>
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


    // Create database from scratch
    
    // $sql = "CREATE DATABASE lab7_db";
    // if (mysqli_query($conn, $sql)) {
    //   echo "Database lab7_db created successfully";
    // } else {
    //   echo "Error creating database: " . mysqli_error($conn);
    // }

    // Create table : Donors(Donor_ID, Aadhar_no, Name, Age, Blood_grp)
    
    // $sql = "CREATE TABLE Donors (
    //     donor_id INT(6) PRIMARY KEY,
    //     donor_aadharNo VARCHAR(30) NOT NULL,
    //     donor_name VARCHAR(30) NOT NULL,
    //     donor_age INT(2) NOT NULL,
    //     donor_bloodgroup VARCHAR(3) NOT NULL
    //     )";

    //     if (mysqli_query($conn, $sql)) {
    //       echo "Table Donors created successfully";
    //     } else {
    //       echo "Error creating table: " . mysqli_error($conn);
    //     }

    //     mysqli_close($conn);
    

    ?>

    <div class="container">
        <div class="brand-title">INSERT A DONOR 🩸</div>
        <div class="inputs">
            <form action="insert.php" method="post">

                <label>Donor Id</label>
                <input type="number" name="donor_id" placeholder="Enter Donor Id" />
                <label>Aadhar No</label>
                <input type="text" name="donor_aadharNo" placeholder="Enter Donor Aadhar" />
                <label>Name</label>
                <input type="text" name="donor_name" placeholder="Enter Donor Name" />
                <label>Age</label>
                <input type="number" name="donor_age" placeholder="Enter Donor Age" />
                <label>Blood Group</label>
                <input type="text" name="donor_bloodgroup" placeholder="Enter Bloodgroup" />

                <button type="submit">SUBMIT</button>

            </form>
        </div>
    </div>

    <div>
        <button class="donorButton">
            <a href="findDonor.php">FIND A DONOR? </a>
        </button>
    </div>


</body>


</html>