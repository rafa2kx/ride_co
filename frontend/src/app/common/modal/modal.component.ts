import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output, output } from '@angular/core';

@Component({
  selector: 'app-modal',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './modal.component.html',
  styleUrl: './modal.component.css',
})
export class ModalComponent {
  @Input() title: string | undefined;
  @Input() showClose: boolean | undefined;
  @Output() onCloseEvent = new EventEmitter();
  close() {
    this.onCloseEvent.emit();
  }
}
