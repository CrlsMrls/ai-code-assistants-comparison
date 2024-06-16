import { Component, inject } from '@angular/core';
import { RouterModule } from '@angular/router';

import { componentList } from '@app/component-list';
import { NavigationService } from '@app/services/header.service';

@Component({
  standalone: true,
  templateUrl: './list.component.html',
  imports: [RouterModule],
})
export class ListComponent {
  #headerService: NavigationService = inject(NavigationService);
  
  items = componentList;

  constructor() {
    this.#headerService.setNavItems([]);
  }



}
