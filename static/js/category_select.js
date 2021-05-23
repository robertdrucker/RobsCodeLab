$(function () {
  $('#category-all').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/All',
    }).done(function () {
      window.location = '/';
    });
  });

  $('#category-css').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/CSS',
    }).done(function () {
      window.location = '/category/CSS';
    });
  });

  $('#category-html').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/HTML',
    }).done(function () {
      window.location = '/category/HTML';
    });
  });

  $('#category-js').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/javaScript',
    }).done(function () {
      window.location = '/category/JavaScript';
    });
  });

  // $('#category-php').click(function(e){
  //   e.preventDefault()
  //   $.ajax({
  //     url: '/blog_category/PHP',
  //     }).done(function() {
  //       window.location = "/category/PHP";
  //     });
  // });

  $('#category-python').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/Python',
    }).done(function () {
      window.location = '/category/Python';
    });
  });

  $('#category-sql').click(function (e) {
    e.preventDefault();
    $.ajax({
      url: '/blog_category/SQL',
    }).done(function () {
      window.location = '/category/SQL';
    });
  });

  // $('#category-misc').click(function (e) {
  //   e.preventDefault();
  //   $.ajax({
  //     url: '/blog_category/Misc',
  //   }).done(function () {
  //     window.location = '/category/Misc';
  //   });
  // });
});
