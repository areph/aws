<?php
header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT"); // Date in the past
?>
<!DOCTYPE html>
<html>

<head>
  <title>EC2 Auto Scaling Test</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="font-sans text-lg">
  <div class="container mx-auto m-10">
    <div class="bg-slate-300 p-10 rounded-lg">
      <?php include("show-instance.php"); ?>
    </div>
  </div>

</body>

</html>