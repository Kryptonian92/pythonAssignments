import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'US Time Zone Display';
  date = new Date();
  newDate = null;
  currentDate(timezone){
    this.date = new Date();
    if (timezone === 'MST'){
      this.date.setHours(this.date.getHours() +1);
    } else if (timezone === 'PST'){
      this.date.setHours(this.date.getHours() + 2);
    }else if (timezone === 'CST'){
      this.date.setHours(this.date.getHours() + 3);
    }else if (timezone === 'EST'){
      this.date.setHours(this.date.getHours() + 4);
    }
    this.newDate = timezone;
    console.log("The Current Time Is:", this.date);
  }
}
