$(function() {
	$('.dropdown-toggle').dropdown();
	$('#dropdown-login-form').click(function(e) {
		e.stopPropagation();
	});
});
