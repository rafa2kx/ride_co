import { Component } from '@angular/core';
import { ModalComponent } from '../../common/modal/modal.component';
import { GoogleLoginComponent } from './google-login/google-login.component';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [ModalComponent, GoogleLoginComponent],
  template: ` <app-modal [title]="'Authentication Required'">
    <h2 class="text-center">Please Login to access your Groceries Lists</h2>
    <div class="w-full flex justify-center">
      <app-google-login />
    </div>
  </app-modal>`,
})
export class AuthComponent {}
