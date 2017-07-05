import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Switchboard';
  text = "The button has been clicked"
  num = 1
  imageArray = [];
  onClick(){
    console.log(this.text, this.num, "Times");
  }
}
