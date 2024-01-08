<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../static/img/favicon.ico">
    <link rel="apple-touch-icon" href="../static/img/icon.png">

    <title>Random Travelers</title>

    <!-- Bootstrap core CSS v4.4.1 -->
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">

    <!-- Custom styles for this template -->
    <link rel="stylesheet" href="/static/css/style.css">

  </head>

  <body>

    <!-- menu -->
    <h1> ${ctx} </h1>
    <div class="container fixed-top" style="top:3%;">
      <div class="row">
        <div class="col-md-3">
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body" style="padding:10px;">
              <img src="../static/img/icon.png" style="width:40px; margin-right:5px; margin-bottom:5px; border-radius: 50%;">
              <h4 class="card-title" id="title" style="display:inline-block;">Random Travelers</h4>
              <p class="card-text" id="describe">Random travelers will support your trip. You can choose a one-way time limit and travel cost limit.</p>
              <h4 class="card-title" id="country" style="color:dodgerblue; display:none;"></h4>
              <h4 class="card-title" id="country-ja" style="color:dodgerblue; display:none;"></h4>
              <div class="container">
                <div class="row">
                  <div class="col-xs-8" style="padding:5px;">
                    <select class="custom-select w-100" id="time" required>
                      <option value="6">6 hour </option>
                      <option value="12">12 hour</option>
                      <option value="18">18 hour</option>
                      <option value="24">24 hour </option>
                      <option value="upper">upper</option>
                    </select>
                  </div>
                  <div class="col-xs-8" style="padding:5px;">
                    <select class="custom-select w-100" id="amount" required>
                      <option value="1000">$ 1,000</option>
                      <option value="2000">$ 2,000</option>
                      <option value="3000">$ 3,000</option>
                      <option value="4000">$ 4,000</option>
                      <option value="5000">$ 5,000</option>
                      <option value="upper">upper</option>
                    </select>
                  </div>
                  <div class="col-xs-8" style="padding:5px;">
                    <button type="button" class="btn btn-primary" onclick="gacha()" style="background:dodgerblue; border-color:dodgerblue;">Go!</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3">
        </div>
      </div>
    </div>


    <!-- Google Map -->
    <div id="map"></div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="/static/js/bootstrap.bundle.min.js"></script>
    <script src="/static/js/script.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/static/js/ie10-viewport-bug-workaround.js"></script>

    <!-- Google Map -->
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBOokebHRajnbQ3vys-YCgEVkgOEJjRq0o&language=ja"></script>

  </body>
</html>
