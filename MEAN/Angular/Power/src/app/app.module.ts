import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MyComponentComponent } from './my-component/my-component.component';
import { PowerComponent } from './power/power.component';
import { HumanComponent } from './power/human/human.component';
import { SaiyanComponent } from './power/saiyan/saiyan.component';
import { SuperSaiyanComponent } from './power/super-saiyan/super-saiyan.component';
import { SuperSaiyan2Component } from './power/super-saiyan2/super-saiyan2.component';
import { SuperSaiyan3Component } from './power/super-saiyan3/super-saiyan3.component';
import { SuperSaiyan4Component } from './power/super-saiyan4/super-saiyan4.component';

@NgModule({
  declarations: [
    AppComponent,
    MyComponentComponent,
    PowerComponent,
    HumanComponent,
    SaiyanComponent,
    SuperSaiyanComponent,
    SuperSaiyan2Component,
    SuperSaiyan3Component,
    SuperSaiyan4Component
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }