$(document).ready(function () {
  $('.drop-down').click(() => {
    $('.drop-links').toggleClass('active');
  });

  $('#show-categories').click(() => {
    $('.category-list').addClass('active');
    $('.overlay').addClass('active');
  });
  $('#remove-category').click(() => {
    $('.category-list').removeClass('active');
    $('.overlay').removeClass('active');
  });

  const lightMode = () => {
    $('.bi-sun').hide();
    $('.bi-moon').show();
    $('body').addClass('light');
    $('body').removeClass('dark');
  };
  const darkMode = () => {
    $('.bi-sun').show();
    $('.bi-moon').hide();
    $('body').addClass('dark');
    $('body').removeClass('light');
  };

  const toggleheme = () => {
    let theme = localStorage.getItem('THEME');
    if (theme === null ? (theme = 'LIGHT') : theme);

    if (theme === 'DARK') {
      darkMode();
    }
    if (theme === 'LIGHT') {
      lightMode();
    }
  };

  toggleheme();

  $('.theme').click(() => {
    if ($('body').hasClass('light')) {
      darkMode();
      localStorage.setItem('THEME', 'DARK');
    } else if ($('body').hasClass('dark')) {
      lightMode();
      localStorage.setItem('THEME', 'LIGHT');
    }
  });
});
