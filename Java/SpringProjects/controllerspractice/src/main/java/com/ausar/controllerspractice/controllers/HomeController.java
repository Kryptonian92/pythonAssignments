package com.ausar.controllerspractice.controllers;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RestController;
//@RestController
@Controller
public class HomeController {
    @RequestMapping("/")
    public String index() {
        return "forward:/index.html";
    }
    
//    @RequestMapping("/world")
//    public String world() {
//        return "Class level annotations are cool too!";
//    }
}