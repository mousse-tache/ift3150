<?php

/**
* 
*/
class BiBlerProxy
{
	private $instance;
	private $url;

	function __construct()	{}

	function setURL($uri) {
		$url=$uri;
	}

	static function getInstance() {
		if (!$instance) {
			$instance=new BiBlerProxy();
		}
			
			return $instance;
		
		
	}


	private function httpPost($url, $data)
	{

		$ch = curl_init( $url );
		curl_setopt( $ch, CURLOPT_POST, 1);
		curl_setopt( $ch, CURLOPT_POSTFIELDS, urlencode($data));
		curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1);
		curl_setopt( $ch, CURLOPT_HEADER, 0);
		curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);

		$response = curl_exec( $ch );
	    return $response;
	}

	function addEntry($data) {
		return httpPost($url."addentry/",$data);
	}

	function getBibtex($data) {
		return httpPost($url."getbibtex/",$data);
	}

	function formatBibtex($data) {
		return httpPost($url."formatbibtex/",$data);
	}

	function previewEntry($data) {
		return httpPost($url."previewentry/",$data);
	}

	function validateEntry($data) {
		return httpPost($url."validateentry/",$data);
	}


}