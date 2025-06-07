package com.RestMethods;

import java.util.concurrent.TimeUnit;

import org.testng.Assert;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class GetWithNonBDD {
  @Test
  public void getSingleUserDetails() {
	  RestAssured.baseURI = "https://reqres.in/api"; // baseURI
	  Response res = RestAssured.get("/users/2");
	  int statuscode = res.getStatusCode();
	  Assert.assertEquals(statuscode, 200, "Status code is not matched!");
	  System.out.println("Status code is matched!"+statuscode);
	  System.out.println("Status Line: "+res.getStatusLine());
	  System.out.println("*****Response in String***********");
	  System.out.println(res.asString());
	  System.out.println("*****Response in formatted like JSON***********");
	  System.out.println(res.asPrettyString());
	  System.out.println("Time for response: "+res.getTime());
	  System.out.println(res.getHeader("Content-Type"));
	  System.out.println("Time in miliseconds: "+res.getTimeIn(TimeUnit.MILLISECONDS));
  }
}
[RemoteTestNG] detected TestNG version 7.4.0
Status code is matched!200
Status Line: HTTP/1.1 200 OK
*****Response in String***********
{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral","text":"Tired of writing endless social media content? Let Content Caddy generate it for you."}}
*****Response in formatted like JSON***********
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}
Time for response: 1266
application/json; charset=utf-8
Time in miliseconds: 1266
PASSED: getSingleUserDetails
***********************************************************************************************************
package com.RestMethods;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class GetWithNonBDD {

    @BeforeClass
    public void setup() {
        RestAssured.baseURI = "https://reqres.in/api";
    }

    @Test
    public void getSingleUserDetails() {
        Response res = RestAssured.get("/users/2");
        int statuscode = res.getStatusCode();
        Assert.assertEquals(statuscode, 200, "Status code is not matched!");
        System.out.println("Status code is matched! " + statuscode);
        System.out.println("Status Line: " + res.getStatusLine());
        System.out.println("***** Response as Raw String ***********");
        System.out.println(res.asString());
        System.out.println("***** Pretty JSON ***********");
        System.out.println(res.asPrettyString());
        System.out.println("Response Time: " + res.getTime());
        System.out.println("Content-Type Header: " + res.getHeader("Content-Type"));
        System.out.println("Time in ms: " + res.getTimeIn(TimeUnit.MILLISECONDS));
    }

    @Test
    public void validateSingleUser() {
        Response res = RestAssured.get("/users/2");
        int id = res.jsonPath().getInt("data.id");
        System.out.println("Id is: " + id);
        String email = res.jsonPath().getString("data.email");
        Assert.assertEquals(email, "janet.weaver@reqres.in", "Email does not match!");
        System.out.println("Email Id is: " + email);
    }

    @Test
    public void getListOfUsers() {
        Response res = RestAssured.get("/users?page=2");
        Assert.assertEquals(res.getStatusCode(), 200, "Expected status code 200");
        System.out.println("***** List of Users (Page 2) ***********");
        System.out.println(res.asPrettyString());

        List<Integer> listOfId = res.jsonPath().getList("data.id");
        System.out.println("Total Id's: " + listOfId.size());
        for (Integer i:listOfId) {
        	System.out.println("List of Id's are: "+i);
        }
    }
}
[RemoteTestNG] detected TestNG version 7.4.0
***** List of Users (Page 2) ***********
{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}
Total Id's: 6
List of Id's are: 7
List of Id's are: 8
List of Id's are: 9
List of Id's are: 10
List of Id's are: 11
List of Id's are: 12
Status code is matched! 200
Status Line: HTTP/1.1 200 OK
***** Response as Raw String ***********
{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral","text":"Tired of writing endless social media content? Let Content Caddy generate it for you."}}
***** Pretty JSON ***********
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}
Response Time: 164
Content-Type Header: application/json; charset=utf-8
Time in ms: 164
Id is: 2
Email Id is: janet.weaver@reqres.in
PASSED: getListOfUsers
PASSED: getSingleUserDetails
PASSED: validateSingleUser

===============================================
    Default test
    Tests run: 3, Failures: 0, Skips: 0
===============================================
***********************************************************************************************************
package com.RestMethods;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class GetWithNonBDD {

    @BeforeClass
    public void setup() {
        RestAssured.baseURI = "https://reqres.in/api";
    }

    @Test
    public void getSingleUserDetails() {
        Response res = RestAssured.get("/users/2");
        int statuscode = res.getStatusCode();
        Assert.assertEquals(statuscode, 200, "Status code is not matched!");
        System.out.println("Status code is matched! " + statuscode);
        System.out.println("Status Line: " + res.getStatusLine());
        System.out.println("***** Response as Raw String ***********");
        System.out.println(res.asString());
        System.out.println("***** Pretty JSON ***********");
        System.out.println(res.asPrettyString());
        System.out.println("Response Time: " + res.getTime());
        System.out.println("Content-Type Header: " + res.getHeader("Content-Type"));
        System.out.println("Time in ms: " + res.getTimeIn(TimeUnit.MILLISECONDS));
    }

    @Test
    public void validateSingleUser() {
        Response res = RestAssured.get("/users/2");
        int id = res.jsonPath().getInt("data.id");
        System.out.println("Id is: " + id);
        String email = res.jsonPath().getString("data.email");
        Assert.assertEquals(email, "janet.weaver@reqres.in", "Email does not match!");
        System.out.println("Email Id is: " + email);
    }

    @Test
    public void getListOfUsers() {
        Response res = RestAssured.get("/users?page=2");
        Assert.assertEquals(res.getStatusCode(), 200, "Expected status code 200");
        System.out.println("***** List of Users (Page 2) ***********");
        System.out.println(res.asPrettyString());
        List<Integer> listOfId = res.jsonPath().getList("data.id");
        System.out.println("Total Id's: " + listOfId.size());
        for (Integer i:listOfId) {
        	System.out.println("List of Id's are: "+i);
        }
    }
    @Test
    public void createUser_post() {
    	RestAssured.baseURI = ("https://reqres.in/api");
    	RestAssured.given().body("{\n"
    			+ "    \"name\": \"morpheus\",\n"
    			+ "    \"job\": \"leader\"\n"
    			+ "}");
    	Response res = RestAssured.post("/users");
    	System.out.println("Status code of createUser_post is: "+res.getStatusCode());
    }
}
[RemoteTestNG] detected TestNG version 7.4.0
Status code of createUser_post is: 415
PASSED: createUser_post
===============================================
    Default test
    Tests run: 1, Failures: 0, Skips: 0
===============================================
===============================================
Default suite
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
===============================================
***********************************************************************************************************
  
***********************************************************************************************************
***********************************************************************************************************
  
***********************************************************************************************************
***********************************************************************************************************
  
***********************************************************************************************************
***********************************************************************************************************
  
***********************************************************************************************************
***********************************************************************************************************
  
***********************************************************************************************************
