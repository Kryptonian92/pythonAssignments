import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Random Barcode Generator'
  imageArray = [];

  Image() {
    for (let y = 0; y < 8; y++) {
      const randNum = (Math.floor(Math.random() * 7) ) + 1;
      if (randNum === 1) {
        this.imageArray.push('Green');
      } else if (randNum === 2) {
        this.imageArray.push('LightBlue');
      } else if (randNum === 3) {
        this.imageArray.push('Red');
      } else if (randNum === 4) {
        this.imageArray.push('Yellow');
      } else if (randNum === 5) {
        this.imageArray.push('Blue');
      } else if (randNum === 6) {
        this.imageArray.push('Orange');
      } else if (randNum === 7) {
        this.imageArray.push('IndianRed');
      } else if (randNum === 8) {
      this.imageArray.push('Pink');
      }
    }
  }

  ngOnInit() {
    this.Image();
  }

}
