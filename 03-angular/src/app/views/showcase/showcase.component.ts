import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { componentList } from '@app/component-list';
import { NavigationService } from '@services/header.service';

import { ButtonComponent } from '@components/button/button.component';
import { CardComponent } from '@components/card/card.component';
import { ButtonGroupComponent } from '@components/button-group/button-group.component';
import { RadioGroupComponent } from '@components/radio/radio-group.component';

@Component({
  standalone: true,
  imports: [ButtonComponent, CardComponent, ButtonGroupComponent, RadioGroupComponent],
  selector: 'showcase',
  templateUrl: './showcase.component.html',
})
export class ShowcaseComponent implements OnInit {
  #activeRoute: ActivatedRoute = inject(ActivatedRoute);
  #router: Router = inject(Router);
  #headerService: NavigationService = inject(NavigationService);
  
  component: any; 
  sizes = ['xs', 'sm', 'md', 'lg', 'xl'];

  ngOnInit(): void {
    const componentId = this.#activeRoute.snapshot.paramMap.get('component') || '';
    const component = componentList.find( comp => comp.url === componentId);    
    // if component is not in componentList, redirect to 404
    if (!component) {
      this.#router.navigate(['/404']);
      return;
    }
    this.#headerService.setNavItems([
      { title: component.name, path: `/component/${component.url}` },
    ]);

    this.component = component;

  }

  onButtonClick(text: string) {
    console.log('button clicked: ', text);
  }

  onGroupSelected(text: number) {
    console.log('button group selected: ', text);
  }

  onRadioSelected(text: number) {
    console.log('radio selected: ', text);
  }

}