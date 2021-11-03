<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InsertResults</title>
</head>

<body>

    <?php
    include 'config.php';

    $servername = "localhost";
    $username = "root";
    $password = $adminPassword;
    $database = "lab7_db";

    $u_donor_id = $_POST["donor_id"];
    $u_donor_aadharNo = $_POST["donor_aadharNo"];
    $u_donor_name = $_POST["donor_name"];
    $u_donor_age = $_POST["donor_age"];
    $u_donor_bloodgroup = $_POST["donor_bloodgroup"];

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $database);

    // Check connection
    if (!$conn) {
        die("Connection to MySQL failed: " . mysqli_connect_error());
    }
    echo "<div>Connected to MySQL successfully!!</div>";

    $sql = "INSERT INTO Donors (donor_id, donor_aadharNo, donor_name, donor_age, donor_bloodgroup)
VALUES ($u_donor_id, '$u_donor_aadharNo', '$u_donor_name',  $u_donor_age, '$u_donor_bloodgroup' )";

    if ($conn->query($sql) === TRUE) {
        echo "<div>New Donor record created successfully</div>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    ?>

</body>

</html>