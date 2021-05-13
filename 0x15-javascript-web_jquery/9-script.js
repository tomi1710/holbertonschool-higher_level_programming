$(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    $.get(url, function (data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
