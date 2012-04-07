$(function() {
	var face_url_e = $("input#face_url");
	var url_prefix = window.location.protocol + "//" + window.location.host;
	$("a").click(function() {
		var url = url_prefix + $(this).attr('href');
		face_url_e.val(url);
		face_url_e.select();
		return false;
	});
});