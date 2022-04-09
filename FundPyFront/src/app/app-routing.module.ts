import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PortfolioListComponent } from './components/portfolio-list/portfolio-list.component';
import { PortfolioDetailsComponent } from './components/portfolio-details/portfolio-details.component';
import { AddPortfolioComponent } from './components/add-portfolio/add-portfolio.component';

const routes: Routes = [
  { path: '', redirectTo: 'portfolios', pathMatch: 'full' },
  { path: 'portfolios', component: PortfolioListComponent },
  { path: 'portfolios/:id', component: PortfolioDetailsComponent },
  { path: 'add', component: AddPortfolioComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
