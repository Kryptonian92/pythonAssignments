package com.ausar.displaydate;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {
	@RequestMapping("/")
	public String index(){
		return "index.jsp";
	}
	@RequestMapping("/time")
	public String time(Model model){
	    Date date = new Date();  
	    SimpleDateFormat formatter = new SimpleDateFormat("hh:mm a");
		model.addAttribute("time",formatter.format(date));
		return "time.jsp";
	}
	@RequestMapping("/date")
	public String date(Model model){
	    Date date = new Date();  
	    SimpleDateFormat formatter = new SimpleDateFormat("EEEE, 'the' dd 'of' MMMM, yyyy");
		model.addAttribute("time",formatter.format(date));
		return "date.jsp";
	}
}