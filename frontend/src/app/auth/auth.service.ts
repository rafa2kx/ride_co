import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ServiceBase } from '../../shared/service.base';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService extends ServiceBase {
  constructor(private httpClient: HttpClient) {
    super();
  }

  authenticate(token: string) {
    const url = `${environment.apiUrl}/auth`; // Replace with your backend URL
    return this.pipeError(
      this.httpClient.post(url, { token }, this.httpOptions)
    );
  }
}
