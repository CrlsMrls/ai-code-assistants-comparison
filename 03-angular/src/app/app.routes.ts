import { NgModule } from '@angular/core';
import {
  PreloadAllModules,
  RouterModule,
  Routes,
} from '@angular/router';

import { NotFoundComponent } from './views/notfound/notfound.component';
import { ShowcaseComponent } from './views/showcase/showcase.component';
import { ListComponent } from './views/list/list.component';



export const routes: Routes = [
  { path: '', component: ListComponent },
  {
    path: 'component/:component',
    component: ShowcaseComponent,
  },
  { path: '404', component: NotFoundComponent },
  { path: '**', redirectTo: '' }, // The wildcard '**' matches any path
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, {
      preloadingStrategy: PreloadAllModules,
    }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
