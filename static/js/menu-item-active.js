$(document).ready(function () {
  // $(".nav li").removeClass("active");//this will remove the active class from
  //previously active menu item
  // $('a[href="' + this.location.pathname + '"]').parents('li,ul').addClass('active');

  $('.nav__link').removeClass('nav__link--active');
  $('.categories__link').removeClass('categories__link--active');

  let pathname = this.location.pathname;

  if (pathname.includes('/tag') && pathname.includes('/category')) {
    const subPathname = pathname.split('/tag');
    pathname = subPathname[0];
  } else if (pathname.includes('/tag')) {
    pathname = '/';
  }

  switch (pathname) {
    case '/':
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    case '/about':
      $('#menu-item-about').addClass('nav__link--active');
      break;
    case '/contact':
      $('#menu-item-contact').addClass('nav__link--active');
      break;
    case '/login':
      $('#menu-item-login').addClass('nav__link--active');
      break;
    case '/register':
      $('#menu-item-register').addClass('nav__link--active');
      break;
    default:
      break;
  }

  switch (pathname) {
    case '/':
      $('#category-all').addClass('categories__link--active');
      break;
    case '/category/CSS':
      $('#category-css').addClass('categories__link--active');
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    case '/category/HTML':
      $('#category-html').addClass('categories__link--active');
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    case '/category/JavaScript':
      $('#category-js').addClass('categories__link--active');
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    // case '/category/PHP':
    //   $("#category-php").addClass("categories__link--active")
    //   $("#menu-item-posts").addClass("nav__link--active")
    // break;
    case '/category/Python':
      $('#category-python').addClass('categories__link--active');
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    case '/category/SQL':
      $('#category-sql').addClass('categories__link--active');
      $('#menu-item-posts').addClass('nav__link--active');
      break;
    // case '/category/Misc':
    //   $('#category-misc').addClass('categories__link--active');
    //   $('#menu-item-posts').addClass('nav__link--active');
    //   break;
    default:
      break;
  }
});
