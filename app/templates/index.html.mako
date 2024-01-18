<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <link rel="icon" href="/static/img/favicon.ico">
  <link rel="apple-touch-icon" href="/static/img/icon.png">

  <title>Random Travelers</title>

  <link rel="stylesheet" href="/static/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/style.css">
</head>

<body>
  <!-- menu -->
  <div class="container fixed-top menu-wrapper">
    <div class="row justify-content-md-center">

      <div class="col-md-6">
        <div class="card">
          <div class="card-body main-card">

            <img class="bot-icon" src="/static/img/icon.png">
            <h4 class="card-title" id="title">Random Travelers</h4>
            <p class="card-text" id="describe">
              Random travelers will support your trip. You can choose a one-way time limit and travel cost limit.
            </p>

            <h4 class="card-title country" id="country"></h4>
            <h4 class="card-title country" id="country-ja"></h4>


            <div class="container">
              <div class="row">
                <div class="col-xs-8 user-opt">
                  <select class="custom-select w-100" id="time" required>
                    % for time in ctx['time']:
                    <option value="${time}">${time} hour </option>
                    % endfor
                    <option value="upper">upper</option>
                  </select>
                </div>
                <div class="col-xs-8 user-opt">
                  <select class="custom-select w-100" id="amount" required>
                    % for amount in ctx['amount']:
                    <option value="${amount}">$ ${amount}</option>
                    % endfor
                    <option value="upper">upper</option>
                  </select>
                </div>
                <div class="col-xs-8 shuffle-button">
                  <button type="button" class="btn btn-primary shuffle" onclick="executeShuffle()">Go!</button>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

    </div>
  </div>


  <!-- Google Map -->
  <div id="map"></div>


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
