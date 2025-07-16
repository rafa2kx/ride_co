import { Component, EventEmitter, Output } from '@angular/core';
import { ModalComponent } from '../../common/modal/modal.component';
import { GoogleLoginComponent } from './google-login/google-login.component';
import { User } from '../../shared/interfaces';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [ModalComponent, GoogleLoginComponent],
  template: ` <app-modal
    [title]="'Authentication Required'"
  >
    <h2 class="text-center">Please Login to access your Groceries Lists</h2>
    <div class="w-full flex justify-center">
      <app-google-login (loggedInEvent)="handleLogin($event)" />
    </div>
  </app-modal>`,
})
export class AuthComponent {
  @Output() loggedInEvent = new EventEmitter<User>();
  handleLogin(user: User) {
    this.loggedInEvent.emit(user);
  }
}
