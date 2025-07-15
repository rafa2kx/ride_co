import {
  AfterViewInit,
  Component,
  EventEmitter,
  NgZone,
  Output,
} from '@angular/core';
import { AuthService } from '../../auth.service';
import { environment } from '../../../../environments/environment';
import { User } from '../../../shared/interfaces';
import { ActivatedRoute } from '@angular/router';
declare const google: any;
@Component({
  selector: 'app-google-login',
  standalone: true,
  imports: [],
  template: `<div id="google-signin-btn" class="m-2"></div>`,
})
export class GoogleLoginComponent implements AfterViewInit {
  @Output() loggedInEvent = new EventEmitter<User>();
  familyId: number | undefined;
  constructor(
    private authService: AuthService,
    private ngZone: NgZone,
    private route: ActivatedRoute
  ) {
    this.route.queryParamMap.subscribe((params) => {
      const familyParam = params.get('familyId');
      if (familyParam) {
        this.familyId = parseInt(familyParam);
      }
    });
  }
  ngAfterViewInit(): void {
    google.accounts.id.initialize({
      client_id: environment.googleClientId,
      callback: (response: any) => {
        this.ngZone.run(() => {
          this.handleCredentialResponse(response);
        });
      },
    });

    google.accounts.id.renderButton(
      document.getElementById('google-signin-btn'),
      { theme: 'outline', size: 'large' }
    );
  }

  handleCredentialResponse(response: any) {
    this.authService
      .authenticate(response.credential, this.familyId)
      .subscribe({
        next: (res) => {
          console.log('Authentication successful:', res);
          this.authService.setUser(res.data);
          this.loggedInEvent.emit(res.data);
        },
        error: (err) => {
          console.error('Authentication failed:', err);
        },
      });
  }
}
