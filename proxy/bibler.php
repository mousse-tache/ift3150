<?php

/**
* 
*/
class BiBlerProxy
{
	private static $instance;
	private static $url;

	private function __construct()	{}

	public function setURL($uri) {
		$this->url=$uri;
	}

	public static function getInstance() {
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

	public function addEntry($data) {
		return $this->httpPost($this->url."addentry/",$data);
	}

	public function getBibtex($data) {
		return $this->httpPost($this->url."getbibtex/",$data);
	}

	public function formatBibtex($data) {
		return $this->httpPost($this->url."formatbibtex/",$data);
	}

	public function previewEntry($data) {
		return $this->httpPost($this->url."previewentry/",$data);
	}

	public function validateEntry($data) {
		return $this->httpPost($this->url."validateentry/",$data);
	}


}