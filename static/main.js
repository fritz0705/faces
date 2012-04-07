$(function () {
	"use strict";
	var face_url_e = $("input#face_url"),
		url_prefix = window.location.protocol + "//" + window.location.host;

	if (window.location.pathname.match(/[0-9]+$/)) {
		face_url_e.val(window.location.href);
		face_url_e.select();
	}

	$(".face a").click(function () {
		var url = url_prefix + $(this).attr('href');
		face_url_e.val(url);
		face_url_e.select();
		return false;
	});
});
