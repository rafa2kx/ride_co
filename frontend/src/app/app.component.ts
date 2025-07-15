import { Component } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { AuthComponent } from './auth/component/auth.component';
import { CommonModule } from '@angular/common';
import { User } from './shared/interfaces';
import { AuthService } from './auth/auth.service';
import { ModalComponent } from './common/modal/modal.component';
declare const google: any;
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, AuthComponent, ModalComponent],
  providers: [],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'Carto';
  user?: User;
  showSharingModal = false;
  sharingUrl = '';
  constructor(private authService: AuthService) {
    try {
      this.user = this.authService.getUser();
      this.sharingUrl = window.location.origin + '/invite/' + (this.user?.familyId || 0);
    } catch (error) {
      console.error('Error parsing token:', error);
    }
  }

  handleLogin($event: User) {
    this.user = $event;
    this.sharingUrl = window.location.origin + '/invite/' + (this.user?.familyId || 0);
  }
  copyInviteLink() {
    navigator.clipboard
      .writeText(this.sharingUrl)
      .then(() => {
        console.log('Text copied!');
      })
      .catch((err) => {
        console.error('Failed to copy text: ', err);
      })
      .finally(() => (this.showSharingModal = false));
  }
}
