# Project Title

Web service interface for Eprints 3.x. 

## Getting Started

Create directory soap in eprints3/cgi
1. cd `eprints_install/cgi`
2. mkdir `soap`
3. copy MetaDataServ.cgi  SearchServ.cgi putEprint.cgi to `eprints_install/cgi/soap`

### Prerequisites

``` sudo apt-get install libsoap-lite-perl ```


## How to use 


$search = new EpClient();

/**
 * search data, return list id
 */
/* search by title */

$search->fileds = array('title');
$search->key = 'Google';
$result_search = $search->search();


echo "============ Search result ============== ";
var_dump($result_search);


/**
 * get medatada by id item, return list metadata
 */
$search->ids = array('1');
$result_metadata = $search->getMetadata();

echo "============= Metadata result =========== ";
var_dump($result_metadata);
/**
 * put metadata
 */

echo "============= Input items result =========== ";
$search->title = 'Test soap client php 2';
$search->abstract = 'testing soap client php';
$search->creators_name = array(array('family' => 'test family1'), array('family' => 'test family2'));
$search->date = '2012-09-30';
$search->type = 'article';
$search->url_file = 'http://eprints.zu.edu.ua/7799/1/%D0%9C%D0%B0%D1%80%D0%BA%D0%B5%D0%B2%D0%B8%D1%87.pdf';
$result_put = $search->put();
var_dump($result_put);


## Authors

* **Novytskiy Oleksandr ** - *Initial work* - [PurpleBooth](https://github.com/alexukua)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

