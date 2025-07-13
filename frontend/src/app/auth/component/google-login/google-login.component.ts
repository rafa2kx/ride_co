import { AfterViewInit, Component } from '@angular/core';
declare const google: any;
@Component({
  selector: 'app-google-login',
  standalone: true,
  imports: [],
  template: `<div id="google-signin-btn" class="m-2"></div>`,
})
export class GoogleLoginComponent implements AfterViewInit {

  ngAfterViewInit(): void {
    google.accounts.id.initialize({
      client_id: '346850660717-vhu1citk7il7getnanscrki8skcjn1ue.apps.googleusercontent.com',
      callback: this.handleCredentialResponse.bind(this),
    });

    google.accounts.id.renderButton(
      document.getElementById('google-signin-btn'),
      { theme: 'outline', size: 'large' }
    );
  }

  handleCredentialResponse(response: any) {
    console.log('Google JWT:', response.credential);
    localStorage.setItem('token', response.credential);
  }
}