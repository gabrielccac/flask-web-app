console.log('hi');

closeAlert = document.querySelector('.btn-close');
alert = document.querySelector('.alert');

closeAlert.addEventListener('click', function() {
    alert.style.display = 'none';
});

presenca = document.querySelector('.btn-present');

presenca.addEventListener('click', function() {
    presenca.classList.add('disabled');
});